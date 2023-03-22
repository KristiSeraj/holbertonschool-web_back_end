export default function guardrail(mathFunction) {
  const queue = [];
  let value;

  try {
    value = mathFunction();
  } catch (error) {
    queue.push(error);
  } finally {
    queue.push(value);
    queue.push('Guadrail was processed');
  }

  return queue;
}
