public class TimeMap {

        private Dictionary<string, List<(int, string)>> stores;

    public TimeMap() {
        stores = new Dictionary<string, List<(int, string)>>();
    }
    
    public void Set(string key, string value, int timestamp) {
        if (!stores.ContainsKey(key))
            stores[key] = new List<(int, string)>();
        
        stores[key].Add((timestamp, value));
    }
    
    public string Get(string key, int timestamp) {
        if (!stores.ContainsKey(key)) return "";
        
        int l = 0, r = stores[key].Count - 1;
        string res = "";

        while (l <= r) {
            int m = l + ((r - l) / 2);

            if (timestamp < stores[key][m].Item1) {
                r = m - 1;
            } else {
                res = stores[key][m].Item2;
                l = m + 1;
            }
        }

        return res;
    }
}
