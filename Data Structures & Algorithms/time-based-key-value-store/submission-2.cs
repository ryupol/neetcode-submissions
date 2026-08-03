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
        
        string res = "";
        foreach (var (t, value) in stores[key]) {
            if (t <= timestamp) res = value;
        }

        return res;
    }
}
