class Solution {
    public boolean isAnagram(String s, String t) {

        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();

        for (char str : s.toCharArray()){
            if (sMap.containsKey(str)){
                sMap.put(str, sMap.get(str)+1);
            }
            else{
                sMap.put(str, 1);
            }
        }
        for (char str : t.toCharArray()){
            if (tMap.containsKey(str)){
                tMap.put(str, tMap.get(str)+1);
            }
            else{
                tMap.put(str, 1);
            }
        }

        return sMap.equals(tMap);

    }

}