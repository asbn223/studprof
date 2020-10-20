// const realBtn = document.getElementById('real-file');
// const customBtn = document.getElementById('custom-button');
// const customTxt = document.getElementById('custom-text');
//
// customBtn.addEventListener('click', function () {
//     realBtn.click();
// });
//
// realBtn.addEventListener('change', function () {
//     if(realBtn.value){
//         let str = realBtn.value;
//         let startIndex = (str.indexOf('\\') >= 0 ? str.lastIndexOf('\\') : str.lastIndexOf('/'));
//         let filename = str.substring(startIndex);
//         if (filename.indexOf('\\') === 0 || filename.indexOf('/') === 0) {
//             filename = filename.substring(1);
//         }
//         customTxt.innerHTML = filename;
//     }
//     else{
//         customTxt.innerHTML = 'No File Chosen'
//     }
// })