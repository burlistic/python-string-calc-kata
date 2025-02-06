import re

class StringCalc:

    def add(self, numbers_str: str):

        if numbers_str.strip() == "":
            return 0
        

        delimiters = r"[,\n]"

        #check for delimiters
        if "//" in numbers_str:
            #remove starting chars
            numbers_str = numbers_str.replace("//", "")

            if "\n" in numbers_str:
                # get delimiters
                delimiters = numbers_str[:numbers_str.index("\n")]
                #clean up and remove the delimters from the input
                numbers_str = numbers_str[numbers_str.index("\n"):]

        result = 0


        split_numbers = re.split(delimiters, numbers_str)

        for x in split_numbers:
            if x.strip() != "":
                
                contains_negatives = False
                negatives = ""

                number = int(x)
                if number < 0:
                    contains_negatives = True
                    negatives = negatives + x

                if contains_negatives:
                    raise Exception("No negative numbers allowed, string contains - " + negatives)

                result = result + int(x)

        return result