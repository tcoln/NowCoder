#include <iostream>
#include <vector>
#include <numeric>
#include <limits>
#include <stack>

using namespace std;

int maxProfit(vector < int > prices) {
	stack<int> s;
	int maxp = 0;
	int l = prices.size();
	s.push(prices[0]);
	int first = prices[0];
	int i = 1;
	while(!s.empty() && i < l){
		int top = s.top();
		if(prices[i] >= top)
			s.push(prices[i]);
		else{
			if(top - first > maxp)
				maxp = top - first;
			while(!s.empty() && prices[i] < s.top())
				s.pop();
			if(s.empty())
				first = prices[i];
			s.push(prices[i]);
		}
		i += 1;
	}
	if(!s.empty() && s.top() - first > maxp)
		maxp = s.top() - first;
	return maxp;
}


int main() {
    int res;

    int _prices_size = 0;
    cin >> _prices_size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n'); 
    vector<int> _prices;
    int _prices_item;
    for(int _prices_i=0; _prices_i<_prices_size; _prices_i++) {
        cin >> _prices_item;
        cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
        _prices.push_back(_prices_item);
    }
 
    res = maxProfit(_prices);
    cout << res << endl;
    return 0;
}

