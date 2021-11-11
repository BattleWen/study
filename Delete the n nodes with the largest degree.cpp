#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <fstream>

using namespace std;

const int MAXN = 4100;
int G[MAXN][MAXN];
int n, m, k;
int x, y;


void init() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			G[i][j] = 0;
		}
	}
}

int  judge() {
	int n = 4039;
	int* count = new int[n];
	for (int i = 0; i < n; i++) {
		count[i] = 0;
	}
	int max = 0;
	int no = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (G[i][j] == 1) count[i]++;
		}
	}

	for (int i = 0;i < n; i++) {
		if (count[i] > max) max = count[i];
	}

	for (int i = 0;i < n; i++) {
		if (count[i] == max) {
			no = i;
			break;
		}
	}

	return no;
}

//void del(int x) {
//	for (int i = 0;i < n; i++) {
//		G[x][i] = 0;
//		G[i][x] = 0;
//	}
//}

int main() {
	int n = 4039;
	int m = 88234;
	cin >> k;
	//输入需要删除的节点数k
	init();

	FILE* fp;
	fp = freopen("D:\\Desktop\\facebook_combined.txt", "r", stdin);
	for (int i = 0; i < m; i++) {
		cin >> x >> y;
		G[x][y] = 1;
		G[y][x] = 1;
	}
	fclose(fp);
	freopen("CON", "r", stdin);

	while (k--) {
		int cur = judge();
		//返回想要删除的节点编号
		printf("%d\n", cur);
		//del(cur);
		for (int i = 0;i < n; i++) {
			G[cur][i] = 0;
			G[i][cur] = 0;
		}
	}
	
	return 0;
}