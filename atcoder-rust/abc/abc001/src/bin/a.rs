use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        h1: i64,
        h2: i64,
    }
    println!("{}", h1-h2);
}