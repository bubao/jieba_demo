var fs = require('fs');
/**
 * [keyWord description]
 * @type {Array}
 * 把想搜索的词用 “"关键词",”  这种方式写在 “[  ]”  中间，
 * 记得关键词引号后面有英文逗号
 * 引号也是引文的
 */
var keyWord = [
	"本行",
	"人民币",
];

var json = JSON.parse(fs.readFileSync('./getObj.json'));
var Arr = []
for (var i = 0; i < keyWord.length; i++) {
	let get = keyWord[i] + ':' + json[keyWord[i]]
	console.log(get)
	Arr.push(get)
}
//你要的关键词在这里
fs.writeFileSync('keyWord.txt', Arr.join('\n'), 'utf8')