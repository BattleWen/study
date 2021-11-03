#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>

using namespace std;

const int N = 510, INF = 1e9;

int g[N][N];
int n, m, k, x, y, z;

void floyd() {
	for (int k = 1; k <= n; k++) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
			}
		}
	}
}

int main()
{
	//cin >> n >> m >> k;
	cin >> n >> m;
	for (int i = 1; i <= n; i++) { //³õÊ¼»¯
		for (int j = 1; j <= n; j++) {
			if (i == j) g[i][j] = 0;
			else g[i][j] = INF;
		}
	}

	FILE* fp;
	fp = freopen("D:\\Desktop\\Edges.txt", "r", stdin);
	freopen("D:\\Desktop\\output.txt", "w", stdout);

	for (int i = 0; i < m; i++) {

		// scanf("%d%d%d", &x, &y, &z);
		 //g[x][y] = min(g[x][y], z);
		// g[y][x] = min(g[y][x], z);

		cin >> z >> x >> y;
		g[x][y] = min(g[x][y], 1);
		g[y][x] = min(g[y][x], 1);
	}

	fclose(fp);

	floyd();
	//freopen("CON", "r", stdin);

	/*while (k--) {
		scanf("%d%d", &x, &y);
		if (g[x][y] > INF / 2) puts("impossible");
		else printf("%d\n", g[x][y]);
	}*/

	int max = 1;
	for (int i = 0; i < 500; i++) {
		for (int j = 0; j < 500; j++) {
			if (g[i][j] < 2100 && g[i][j] > max)
				max = g[i][j];
		}
	}
	cout << max << endl;

	for (int i = 0; i < 500; i++) {
		for (int j = 0; j < 500; j++) {
			if (g[i][j] == max)
				cout << i << " " <<j << endl;
		}
	}

	fclose(stdout);

	return 0;
}