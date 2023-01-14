<script>
	import {Content} from 'carbon-components-svelte';
	export let bindings;

	let {Car, color} = bindings;   // destructure for easier access

	let c = Car.new();
	c.number = 5;
	c.color = 775577;
	console.log(c);

	let c2 = color(c, 557755);
	console.log(c2.number, c2.color);

	let c3 = c2.duplicate();
	console.log(c3.number, c3.color);
	console.log(c2, c3);

	c3.change_number(99);
	c3.change_color(887766);
	console.log(c3.number, c3.color);
</script>

<Content>
<h1>
{bindings.add(5, 7)}
</h1>
</Content>