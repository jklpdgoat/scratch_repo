import App from './App.svelte';

// User defined imports
import wasm from '../../rust/Cargo.toml';

// const app = new App({
// 	target: document.body,
// 	props: {
// 		name: 'world'
// 	}
// });

// export default app;

const init = async() => {
	const bindings = await wasm();
	const app = new App({
		target: document.body
	});
}