import App from './App.svelte';

// User defined imports
import wasm from '../../rust/Cargo.toml';

// Import carbon components
import "carbon-components-svelte/css/g80.css"

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
		target: document.body,
		props: {
			bindings,
		},
	});
};

init();