#include <cstdlib>
#include <iostream>
#define max 20


using namespace std;
//variable global, 999 merepresentasikan infinity
#define INF 999

// program utama
int main() {
    // inisalisasi variable 
    int i, j, source, target, start, minimum, m, update, ver, min_weight;
     cout << "======================================== \n\n";
     cout << "UNIVERSITAS ISLAM LAMONGAN 2021\n\n";
    cout << "PROGRAM ALGORITMA DIJKSTRA \n\n";
    cout << "======================================== \n\n";
    // masukkan jumlah vertex yang diinginkan
    cout << "Masukkan Jumlah Vertex yang Anda inginkan : "; cin >> ver; ver++;
    // matriks bobot, buffer, visited dll
  int weight[ver][ver], buff[ver], path[ver], prev[ver], visited[ver];
    // nilai awal bobot, buffer, dll
    for(i = 1; i < ver; i++) {
        buff[i] = INF;
        prev[i] = -1;
        path[i] = 0;
        for(int j = 1;j < ver; j++) {
            weight[i][j] = INF;
        }
    }
    // memasukkan nilai bobot
    for(i = 1;i < ver; i++) {
        for(j = i+1; j < ver; j++)
        {
            cout << "Masukkan bobot " << i << " ke " << j << " : "; cin >> weight[i][j];
            weight [j][i] = weight[i][j];
        }    cout << "\n";
    }
    // masukkan vertex awal dan tujuan
    cout << "Masukkan Vertex Awal : "; cin >> source;
    cout << "Masukkan Vertex Tujuan : "; cin >> target;
    
    start = source;
    visited[start]=1;
    buff[start] = 0;
    // proses mencari bobot terkecil 
    while(visited[target] == 0) {
        minimum = INF;
        m = 0;
        for(i=1;i< ver;i++) {
            update = buff[start] + weight[start][i];
            // cek vertex yang sudah dikunjungi
            if(update < buff[i] && visited[i]==0) {
                buff[i] = update;
                prev[i] = start;
            }
            if(minimum > buff[i] && visited[i]==0) {
                minimum = buff[i];
                m = i;
            }
        } 
        start = m;
        visited[start] = 1;
    }
    // bobot terkecil 
    min_weight = buff[target];
    // backtracking untuk mencari jalur yang dilalui
    // mulai backtracking
    start = target;
    j = 0;
    // mencari vertex yang dikunjungi
    while(start != -1) {
        path[j] = start;
        start = prev[start];
        j++;
    }
    // menampilkan bobot terkecil yang dilalui
    cout << "\nBobot terkecil yang dilalui adalah " << min_weight << "\n";
    // menampilkan vertex yang dikunjungi
    cout << "Jalur yang ditempuh adalah : ";
    for (int i = ver-1; i >= 0; i--) {
        if (path[i] != 0) {
            cout << path[i] << " ";
        }

    } cout << "\n";
    cout << "TERIMA KASIH, SELAMAT MENCOBA\n\n";
}