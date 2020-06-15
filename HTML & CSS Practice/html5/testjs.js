/* 번호를 전달받아 이미지를 바꾸기 */
function changeImg(pIndex){
    // 이미지 목록 배열
    var img_names = ["mr0.jpg","mr1.jpg","mr2.jpg"];
    // alert(img_names[pIndex]);
    // alert(document.getElementById("imgM"));
    // 이미지 엘리먼트
    var imgM = document.getElementById("imgM");
    imgM.setAttribute("src", img_names[pIndex]);
}




/* 실행시 네이버로  */
function goNaver(){alert("Hello ! go to NAVER");
// window.location.href
/*
    window. 브라우저창
    location. 주소창
    href. 주소창의 url
*/
window.open('about:blank').location.href="https://www.naver.com/";}
