use itertools::{Itertools, zip};
use std::str::FromStr;
use core::fmt;
use std::borrow::Borrow;

struct Point {
    x: i32,
    y: i32
}

impl FromStr for Point {
    type Err = ();
    fn from_str(s: &str) -> Result<Point, ()> {
        let values = s
            .split(",")
            .map(|x| x.parse::<i32>().unwrap())
            .collect_vec();

        if values.len() != 2 {
            return Err(())
        }

        return Ok(Point {x: values[0], y: values[1]})
    }
}

impl fmt::Debug for Point {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Point")
            .field("x", &self.x)
            .field("y", &self.y)
            .finish()
    }
}

impl Copy for Point { }

impl Clone for Point {
    fn clone(&self) -> Self {
        *self
    }
}

struct Line {
    start: Point,
    end: Point
}


impl FromStr for Line {
    type Err = ();
    fn from_str(s: &str) -> Result<Line, ()> {
        let point_values = s
            .split(" -> ")
            .map(|x| Point::from_str(x).unwrap())
            .collect_vec();

        if point_values.len() != 2 {
            return Err(())
        }

        return Ok(Line {start: point_values[0].clone(), end: point_values[1].clone()})
    }
}

impl fmt::Debug for Line {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Line")
            .field("start_point", &self.start)
            .field("end_point", &self.end)
            .finish()
    }
}

impl Line {
    fn get_points_hor_ver(&self) -> Vec<Point> {
        let x_diff = self.end.x - self.start.x;
        let y_diff = self.end.y - self.start.y;

        let x_sign = 1 - (2 * (x_diff < 0) as i32);
        let y_sign = 1 - (2 * (y_diff < 0) as i32);

        let mut points: Vec<Point> = vec![];

        if x_diff != 0 && y_diff != 0 {
            return points;
        }

        for x_count in 0..x_diff.abs() + 1 {
            for y_count in 0..y_diff.abs() + 1 {
                points.push(Point {
                    x: self.start.x + (x_sign * x_count),
                    y: self.start.y + (y_sign * y_count)
                })
            }
        }

        return points
    }

    fn get_points_hor_ver_dia(&self) -> Vec<Point> {
        let x_diff = self.end.x - self.start.x;
        let y_diff = self.end.y - self.start.y;

        let x_sign = 1 - (2 * (x_diff < 0) as i32);
        let y_sign = 1 - (2 * (y_diff < 0) as i32);

        let mut points: Vec<Point> = vec![];

        if x_diff != 0 && y_diff != 0 && x_diff.abs() != y_diff.abs() {
            return points;
        }

        if x_diff.abs() != y_diff.abs() {
            return self.get_points_hor_ver()
        }

        for (x_count, y_count) in zip(0..x_diff.abs() + 1, 0..y_diff.abs() + 1) {
            points.push(Point {
                x: self.start.x + (x_sign * x_count),
                y: self.start.y + (y_sign * y_count)
            })
        }

        return points
    }
}

pub fn run_01(content: String) {
    let input_str_lines = content
        .split("\n")
        .collect_vec();

    let lines = input_str_lines
        .into_iter()
        .map(|x| Line::from_str(x).unwrap())
        .collect_vec();

    let mut field = [[0;1000];1000];

    let mut fields_above_2_counter = 0;

    for line in lines {
        let points = line.get_points_hor_ver();

        // println!("{:?} Points to add: {}", line, points.len());
        for point in points {
            field[point.y as usize][point.x as usize] += 1;
            fields_above_2_counter += (field[point.y as usize][point.x as usize] == 2) as usize
        }
    }

    /* for row in field {
        println!("{:?}", row);
    }*/
    println!("Number of fields >= 2: {}", fields_above_2_counter);
}

pub fn run_02(content: String) {
    let input_str_lines = content
        .split("\n")
        .collect_vec();

    let lines = input_str_lines
        .into_iter()
        .map(|x| Line::from_str(x).unwrap())
        .collect_vec();

    let mut field = [[0;1000];1000];

    let mut fields_above_2_counter = 0;

    for line in lines {
        let points = line.get_points_hor_ver_dia();

        println!("{:?} Points to add: {}", line, points.len());
        for point in points {
            field[point.y as usize][point.x as usize] += 1;
            fields_above_2_counter += (field[point.y as usize][point.x as usize] == 2) as usize
        }
    }

    /* for row in field {
        println!("{:?}", row);
    }*/
    println!("Number of fields >= 2: {}", fields_above_2_counter);
}