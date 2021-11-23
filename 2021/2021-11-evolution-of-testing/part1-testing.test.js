#!/usr/bin/env node

function add (a, b) {
  return a + b
}
console.log(add(2, 2) === 4)

describe('add: pointless tests', () => {
  test('Integer pointless test, huff', () => {
    expect(add(2, 2)).toEqual(4)
  })
  test('Fractions pointless test, puff', () => {
    expect(add(0.1, 0.2)).toEqual(0.3)
  })
})