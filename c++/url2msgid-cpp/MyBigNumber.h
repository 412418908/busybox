
#ifndef MYBIGNUMBER_H
#define MYBIGNUMBER_H

#include <vector>
#include <string>
#include <iostream>
#include "bignumber.h"
#include "CharIdMap.h"

class MyBigNumber {
public:
   
    MyBigNumber(int radix);
    MyBigNumber(MyBigNumber& val, int radix);
	MyBigNumber(MyBigNumber& val);
	
	void push(int value);
	int pop();
	bool isZero();
	int getRadix(){
		return mRadix.AsDword();
	}
	
	const char* dump(){
		return mNumber.AsHexStr();
	}
	
	
	static std::string number2String(MyBigNumber& num, CharIdMap& idMap);
	
	static void string2Number(const std::string& str, CharIdMap& idMap, MyBigNumber& result);
    
private:
	BigNumber mNumber;
	BigNumber mRadix;
};



#endif