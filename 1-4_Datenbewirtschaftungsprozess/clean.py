import sys
import json
import matplotlib.pyplot as plt


class DataVisualization:

    def __init__(self, filename, key, description):
        self.data = self.read(filename)
        self.key = key
        self.description = description
        self.run()

    def run(self):
        ''' contains the "flow logic" of the programm '''
        data = self.count_key()
        self.draw(data)

    def count_key(self):
        ''' counts the occurrences of the key '''
        counter = {}
        # go through the record with a for each loop. so we can call the
        # dict-elem itself.
        for elem in self.data:
            # the given sector can be wrong, try except block needed.
            try:
                # If the value has already been counted up, increment by 1
                if elem[self.key] in counter:
                    counter[elem[self.key]] += 1
                # if not, put a 1 for the first occurrence
                else:
                    counter[elem[self.key]] = 1
            except:
                print("The given sector is not given")
                ''' The programm will quit explicit.'''
                sys.exit()
        return counter

    def draw(self, data):
        ''' Draws the graph based on the generated data '''
        # create two different types of graphs in one figure
        fig, axs = plt.subplots(2)

        # set the titles
        fig.canvas.set_window_title(self.description[0])
        fig.suptitle(self.description[1])

        # star operator was used so that key and value of dict
        # can be used as a concatenated list. the data are set as
        # graph content
        # @mmv: in Ruhe erklären und Beispiel zeigen

        axs[0].plot(*zip(*data.items()))
        key_list = []
        value_list = []

        for elem in self.data:
            # Elem sind dict, weil die daten in einer liste sind
            for key, value in elem.items():
                key_list = key_list.append(key)
                value_list.append(value)

        axs[0].plot(key_list, value_list)
        axs[1].plot(*zip(*data.items()))

        # Alternativ shorter style
        # axs[0].plot(*zip(*data.items()))
        # axs[1].bar(*zip(*data.items()))

        # the labels may only be written on the outer axes.
        for ax in axs.flat:
            ax.label_outer()

        # the x-axis label must be rotated,
        # otherwise the words will overlap
        plt.xticks(rotation=90)

        # therefore the new (forced) layout has
        # to be adapted. "show me 100% everything"
        plt.tight_layout()
        plt.show()

    def read(self, filename):
        ''' reads a file and outputs the content in json format (dict) '''
        try:
            filepointer = open(filename)
        except OSError:
            import traceback
            print("Could not open file", filename)
            traceback.print_exc()
            sys.exit()
        data = json.load(filepointer)
        filepointer.close()
        return data


if __name__ == "__main__":
    DataVisualization("dscb230-exercise\dummy-matthias\dummy-data.json", "sector", ("DSCB 230",
                                                                                    "Anzahl der verwendeten Sektoren bei der Börse"))
