
#ifndef CHARIDMAP_H
#define CHARIDMAP_H

#include <vector>
#include <string>


class CharIdMap {
public:
   
	static CharIdMap* gUrlMap;
	static CharIdMap* gMsgIdMap;
	static void init();
	
	CharIdMap(const char* charStr, int radix);
	
	int getRadix(){
		return mRadix;
	}
	
	 int idOfChar(char ch);
	
	 char charOfId(int id);
	
private:
    int mRadix;
	char mId2Char[256];
	int mChar2Id[256];
};



#endif