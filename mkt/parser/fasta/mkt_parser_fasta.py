from mkt.core.fragment import Fragment


class Fasta(object):

    @staticmethod
    def from_file(file_name):
        result = []
        seq = ''
        file = open(file_name)
        while True:
            line = file.readline()
            if line == '':
                result.append(Fragment('fasta_{}'.format(str(len(result) + 1)), 5, seq.replace('\n',''), title=line.replace('\n','')))
                return result
            if line.startswith('>'):
                if seq != '':
                    result.append(Fragment('fasta_{}'.format(str(len(result)+1)) ,5, seq.replace('\n',''), title=line.replace('\n','')))
                    seq = '' 
            else:
                seq = seq + line
