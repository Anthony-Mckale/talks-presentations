// BAD
let size = 1000000 * 1
let tic = new Date().valueOf()

let sum = 0
for (let number = 1; number <= size; number++) {
    sum += number
}
console.log(500000000500000000 - sum)

toc = new Date().valueOf()
console.log(`1 to ${size} = ${sum}`)
console.log(`${(toc - tic) / 1000} seconds`)
// 1 to 1000000 = 499999500000
// 0.282 seconds


// // UGLY
// let size = 1000000
// let tic = new Date().valueOf()
//
// let numbers = []
// for (let i = 1; i <= size; i++) {
//     numbers.push(i)
// }
//
// let sum = 0
// for (let number in numbers) {
//     sum += number * 1
// }
//
// toc = new Date().valueOf()
// console.log(`1 to ${size} = ${sum}`)
// console.log(`${(toc - tic) / 1000} seconds`)
// // 1 to 1000000 = 499999500000
// // 0.282 seconds