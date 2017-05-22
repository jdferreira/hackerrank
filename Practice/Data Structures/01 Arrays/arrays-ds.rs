use std::io;
use std::str::FromStr;

fn print_with_space<T, I>(mut it: I)
    where I: Iterator<Item = T>,
          T: std::fmt::Display
{
    if let Some(x) = it.next() {
        print!("{}", x);
        for x in it {
            print!(" {}", x);
        }
    }
}

fn parse<T>(x: &str) -> T
    where T: FromStr + std::fmt::Display,
          <T as std::str::FromStr>::Err: std::fmt::Debug
{
    T::from_str(x).expect(&format!("parse error on {}", x))
}

fn main() {
    let mut buf = String::new();
    io::stdin().read_line(&mut buf).expect("io error");
    buf.clear(); // Ignore the first line

    io::stdin().read_line(&mut buf).expect("io error");
    let mut nums = buf.split_whitespace().map(parse::<u32>).collect::<Vec<_>>();

    nums.reverse();

    print_with_space(nums.iter());
}
