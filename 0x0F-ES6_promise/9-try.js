export default function guardrail(mathFunction) {
  const queue = [];
  let res;

  try {
    res = mathFunction();
  } catch (error) {
    queue.push(error);
  }
  queue.push(res);
  queue.push('Guardrail was processed');
  return queue;
}
