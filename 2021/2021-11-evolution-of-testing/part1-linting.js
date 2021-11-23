#!/usr/bin/env node

console.log('non_zero_string' == true) // 1)
console.log('true' == true) // 2)
console.log([] == true) // 3)
console.log(['true'] == true) // 4)
console.log(['true'] == 'true') // 5)
// console.log(0.1 + 0.2 == 0.3) // 6)

console.log('"non_zero_string" == true : ', 'non_zero_string' == true) // 1)
console.log('"true" == true : ', 'true' == true) // 2)
console.log('[] == true : ', [] == true) // 3)
console.log('["true"] == true : ', ['true'] == true) // 4)
console.log('["true"] == \'true\' : ', ['true'] == 'true') // 5)
console.log('JS counts correctly (0.1 + 0.2 == 0.3)) :', (0.1 + 0.2 == 0.3)) // 6)
