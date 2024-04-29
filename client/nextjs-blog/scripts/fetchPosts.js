export async function fetchPosts()
{
	try {
		const res = await fetch(`http://localhost:3001/posts/`); //ideally not hardcoded but needs must 
		const data = res.json();
		return data
	} catch (err) {
		return {}
	}
};
