use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub struct Car {
    pub number: usize,
    pub color: usize, // Color in hex code
}

#[wasm_bindgen]
impl Car {
    pub fn new() -> Self {
        Car {
            number: 0,
            color: 0,
        }
    }

    pub fn duplicate(&self) -> Self {
        Self {
            number: self.number + 1,
            color: self.color,
        }
    }

    pub fn change_number(&mut self, number: usize) {
        self.number = number;
    }

    pub fn change_color(&mut self, color: usize) {
        self.color = color;
    }
}

#[wasm_bindgen]
pub fn color(a: Car, color: usize) -> Car {
    Car {
        number: a.number,
        color,
    }
}

#[wasm_bindgen]
pub fn add(left: usize, right: usize) -> usize {
    left + right
}

// #[cfg(test)]
// mod tests {
//     use super::*;

//     #[test]
//     fn it_works() {
//         let result = add(2, 2);
//         assert_eq!(result, 4);
//     }
// }
