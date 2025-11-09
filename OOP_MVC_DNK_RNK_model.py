class SequenceModel:
    def __init__(self, seq: str):
        self.seq = "".join(seq.upper().split())

    def validate(self):
        allowed = {"A", "T", "G", "C", "U"}
        return all(ch in allowed for ch in self.seq)

    def gc_content(self):
        gc = sum(1 for ch in self.seq if ch in {"G", "C"})
        return 100 * gc/len(self.seq) if len(self.seq) > 0 else 0

    def transcribe(self):
        return SequenceModel(self.seq.replace("T", "U"))

    def reverse_transcribe(self):
        return SequenceModel(self.seq[::-1].replace("U", "T"))

    def complement(self):
        comp_map=str.maketrans("ATGCU", "TACGA")
        comp=self.seq.translate(comp_map)
        return SequenceModel(comp[::-1])

    def mutate(self, pos: int, new_base: str):
        lst=list(self.seq)
        lst[pos-1]=new_base.upper()
        return SequenceModel("".join(lst))

    def save_fasta(self, path):
        with open(path, "w") as f:
            f.write(">sequence\n")
            f.write(self.seq+"\n")

    @staticmethod
    def load_fasta(path):
        with open(path, "r") as f:
            lines = f.readlines()
        seq="".join(line.strip() for line in lines if not line.startswith(">"))
        return SequenceModel(seq)