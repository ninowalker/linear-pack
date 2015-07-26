from collections import defaultdict
import sys
import re


class Bin(object):
    """ Container for items that keeps a running sum """
    def __init__(self, maxV):
        self.items = []
        self.sum = 0
        self.maxV = maxV

    def append(self, item, extra=0):
        self.items.append(item)
        self.sum += item + extra

    def __str__(self):
        """ Printable representation """
        return 'Bin(sum=%d, remaining=%s, items=%s)' % (self.sum,
                                                        self.maxV - self.sum,
                                                        str(self.items))

    @classmethod
    def pack(cls, values, maxValue, extra=0):
        values = sorted(values, reverse=True)
        bins = []

        for item in values:
            # Try to fit item into a bin
            possible = []
            for bin in bins:
                truev = item + extra
                if bin.sum + truev <= maxValue:
                    possible.append((bin.sum + truev, bin))
                    break
            else:
                # item didn't fit into any bin, start a new bin
                #print 'Making new bin for', item
                bin = Bin(maxValue)
                possible.append((0, bin))
                bins.append(bin)
            bin = sorted(possible, reverse=True)[0][1]
            bin.append(item, extra)
        return bins


class MaterialList(object):
    def __init__(self):
        self.materials = defaultdict(list)

    def load(self, fp):
        for l in fp:
            l = l.strip()
            if not l:
                continue
            if l.startswith("#"):
                continue
            mat, length, count = re.split(r'\s*/\s*', l)
            maxV = 20 * 12
            if "=" in mat:
                mat, maxV = re.split(r'\s*=\s*', mat)
            for i in xrange(int(count)):
                self.materials[(mat, int(maxV))].append(float(length))

    def pack(self, extra=1):
        order = []
        for (key, maxV) in sorted(self.materials.keys()):
            order.append((key, Bin.pack(self.materials[(key, maxV)], maxV, extra)))
        return order


def main(file_):
    mats = MaterialList()
    mats.load(open(file_))
    order = mats.pack()
    for item_, bins in order:
        print item_, ", count =", len(bins),
        print "\n\t", "\n\t".join(map(str, bins))


if __name__ == '__main__':
    main(sys.argv[1])
        
