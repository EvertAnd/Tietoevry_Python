
# def input_model():
#     preferred_model = input("\nIzvēlieties modeli: ")
#
#     return preferred_model
#
#
# model = input_model()
# print(model)

def metodetogetto():
    metodetoget = input("Ievadiet vēlāmo pārvietošanās metodi Auto -"'A'", ar Kājām - ""K"": ")
    all_metods = 'dirBtnDrive dirBtnNormal', 'irBtnWalk dirBtnNormal'
    if metodetoget == "A":
        way = "dirBtnDrive dirBtnNormal"
        # print(way)
        return way
    if metodetoget == "K":
        way = "irBtnWalk dirBtnNormal"
        # print(way)
        return way
    if metodetoget not in all_metods:
        print(metodetoget + " Ievadītā opcija nav pieejama")
        way = metodetogetto()
    return way


selectemetod = metodetogetto()
print(selectemetod)

//*[@id="directionsPanelRoot"]/div/div[2]/div[1]/div[1]/div/div[1]/div/a[2]