// Enter your code here

use std::io;
use std::io::BufRead;

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    let (n, q) = {
        let line = lines.next().unwrap().expect("io error");
        let mut fields = line.split_whitespace().map(|x| str::parse::<usize>(x).expect("io error"));
        (fields.next().unwrap(), fields.next().unwrap())
    };
    
    println!("{:?}", (n, q));
}
