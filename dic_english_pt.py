from collections import OrderedDict
from func_dic_englis_pt import add_word, display_dictionary

if __name__ == "__main__":

        words = [
                ("English", "Portugueses"),
                ("several", "diversas"),
                ("seldom", "raramente"),
                ("predict", "previsao"),
                ("forecasting",  "previsao"),
                ("features", "caracteristicas"),
                ("trend", "tendencia"),
                ("set", "definir"),
                ("peaks", "picos"),
                ("approach", "abordagem"),
                ("cluster", "conjunto"),
                ("current", "atual"),
                ("often", "muitas vezes"),
                ("suitable", "adequado"),
                ("Highlights", "destaques"),
                ("deployment", "implantacao"),
                ("unit", "unidade"),
                ("aim", "mirar"),
                ("clustering", "agrupamento"),
                ("taking", "tirando"),
                ("widespread", "dinfundida"),
                ("fold", "dobrar"),
                ("near", "aproximar"),
                ("tag", "marcação"),
                ("showcase", "mostruario"),
                ("embeds", "incorporações"),
                ("flat", "plana"),
                ("stamps", "selos"),
                ("chunk", "pedaço"),
                ("profiling", "perfil"),
                ("intended", "pretendido/desejado"),
                ("reduced", "reduzida"),
                ("predicting", "prevendo"),
                ("wrapped", "envolta"),
                ("storage", "armazenamento"),
                ("previous", "anterior"),
                ("current", "atual"),
                ("trends", "tendencias"),
                ("meaningful", "significativa"),
                ("label", "classificado"),
                ("surveys", "pesquisas"),
                ("attendees", "participantes"),
                ("deployments", "implantação"),
                ("curating", "curadoria"),
                ("unlike", "diferente"),
                ("stamps", "selos/marca/carimbo")
        ]

        # Create the initial dictionary
        dictionary = {english: portuguese for english, portuguese in words}
        # Initial display
        sorted_dictionary = OrderedDict(sorted(dictionary.items()))
        display_dictionary(sorted_dictionary)

        while True:
                new_english = input("Enter a new English word (or 'q' to quit): ")
                if new_english == "Q".lower():
                        print("Process end")
                        break
                new_portugues = input("Enter a new Portugues word: ")
                sorted_dictionary = add_word(sorted_dictionary, new_english, new_portugues)
                print("\nUpdated dictionary:")
                display_dictionary(sorted_dictionary)
