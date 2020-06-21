use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        m: i64,
    }

    let ans: i64;
    if m < 100 {
        ans = 0;
    } else if m <= 5000 {
        ans = m/100;
    } else if m <= 30000 {
        ans = m/1000 + 50;
    } else if m <= 70000 {
        ans = (m/1000 - 30)/5 + 80;
    } else {
        ans = 89;
    }

    println!("{:02}", ans);
}