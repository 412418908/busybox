

#include <sstream>
#include <stack>
#include <iostream>

#include "MyBigNumber.h"

   
MyBigNumber::MyBigNumber(int radix):mNumber(0),mRadix(radix)
{
	
}
	
MyBigNumber::MyBigNumber(MyBigNumber& val, int radix):mNumber(val.mNumber),mRadix(radix)
{
	
}

MyBigNumber::MyBigNumber(MyBigNumber& val):mNumber(val.mNumber),mRadix(val.getRadix())
{
	
}

void MyBigNumber::push(int value)
{
	mNumber *= mRadix;
	mNumber += value;
}
	
int MyBigNumber::pop()
{
	BigNumber val = mNumber % mRadix;
	mNumber /= mRadix;
	return val.AsDword();
}
	
bool MyBigNumber::isZero()
{
	return mNumber.isZero();
}


 std::string MyBigNumber::number2String(MyBigNumber& num1, CharIdMap& idMap)
 {
	MyBigNumber num(num1);
	std::string result;
	while(true){
		int n = num.pop();
		result.append(1, (char)idMap.charOfId(n));
		if (num.isZero()){
			break;
		}
	}
	std::reverse(result.begin(), result.end()); 
	 return result;
 }
	
 void MyBigNumber::string2Number(const std::string& str, CharIdMap& idMap, MyBigNumber& result)
 {
		const char* chars = str.c_str();
		int len = (int)str.size();
		for (int i=0; i<len; i++){
			int n = idMap.idOfChar(chars[i]);
			result.push(n);
		}
		
 }
	

	