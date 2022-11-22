def sellorbuy(prediksi):
    urutprediksi = sorted(prediksi)
    a = list(reversed(urutprediksi))

    modal = 0
    hasil = 0
    saham = 0
    itr = 0

    for i in range(0, len(prediksi)):
        if prediksi[i] < a[itr]:
            modal += prediksi[i]
            hasil += 1
        
        else:
            saham += hasil * prediksi[i]
            saham -= modal
            hasil = 0
            modal = 0
            itr += 1
        
    return saham

banyak = int(input())
prediksi = list(map(int,input().strip().split()))[:banyak]

print(sellorbuy(prediksi))