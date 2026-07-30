class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()){
            return false;
        }

        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();

        
        for (int i = 0; i < s.length(); i++){
            
            Character strS = s.charAt(i);
            Character strT = t.charAt(i);
            if (sMap.containsKey(strS)){
                sMap.put(strS, sMap.get(strS)+1);
            }
            else{
                sMap.put(strS, 1);
            }

            if (tMap.containsKey(strT)){
                tMap.put(strT, tMap.get(strT)+1);
            }
            else{
                tMap.put(strT, 1);
            }
        }
        

        return sMap.equals(tMap);

    }

}