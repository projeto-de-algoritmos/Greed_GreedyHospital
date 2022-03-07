
class Surgery:
    def __init__(self, procedure, head_of_surgery, start_time, end_time):
        self.procedure = procedure
        self.head_of_surgery = head_of_surgery
        self.start_time = start_time
        self.end_time = end_time

    def print_data(self):
        print(f"Procedure {self.procedure}")
        print(f"Head of surgery {self.head_of_surgery}")
        print(f"Start: {self.start_time}")
        print(f"End {self.end_time}")

    def return_data(self):
        s = ""
        s += f"\nProcedure {self.procedure}\n"
        s += f"Head of surgery {self.head_of_surgery}\n"
        s += f"Day: 0{ self.start_time // 24 }/01, Hour:{ self.start_time % 24 } \n"
        return s
