/**
 * Hello World を標準出力に表示する
 */
function greetWorld(): void {
  console.log("Hello World");
}

// 直接実行する場合
if (require.main === module) {
  greetWorld();
}

export default greetWorld;
