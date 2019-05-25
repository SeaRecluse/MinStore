



input_seq_cut = ["大","月","亮"]
list_orig_Q_cut = [["小","月","亮"],["方","月","亮"],["中","月","亮"]]

for n in range(0,len(list_orig_Q_cut)):
        word_set = set(input_seq_cut).union(set(list_orig_Q_cut[n]))        
        word_dict = dict()

        i = 0
        for word in word_set:
            word_dict[word] = i
            i += 1
        input_seq_cut_code = [word_dict[word] for word in input_seq_cut]
        
        print(input_seq_cut_code)
        print("*******************************************")
        input_seq_cut_code = [0]*len(word_dict)

        print(input_seq_cut_code)

        for word in input_seq_cut:
            input_seq_cut_code[word_dict[word]]+=1

        print(input_seq_cut_code)

        print("--------------------------------------------")