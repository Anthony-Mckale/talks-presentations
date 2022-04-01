use std::time::{Instant};

fn main() {
    println!("helloworld");
    let now = Instant::now();

    let mut sum:usize = 0;
    let mut i:usize = 0;
    while i < 1000000001 {
        sum = sum + i;
        i = i + 1;
    }
    println!("1 to {} = {}", 1000000000, sum);

    // UGLY
    // const SIZE:usize = 1000000;
    // let mut sum:usize = 0;
    // for i in 1..SIZE {
    //     sum = sum + i;
    // }
    // sum = sum + SIZE;
    // println!("1 to {} = {}", SIZE, sum);

    let elapsed_time = now.elapsed();
    println!("took {} ms", elapsed_time.as_millis());
    // 1 to 1000000 = 499999500000
    // 0.282 seconds
}
