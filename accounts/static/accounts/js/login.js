window.onload = function() {
    if(getCookie("id")) {
        document.loginForm.username.value = getCookie("id");
        document.loginForm.isSave.checked = true;
    }
}

// 주어진 이름의 쿠키를 반환하는데,
// 조건에 맞는 쿠키가 없다면 undefined를 반환합니다.
function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function setCookie(name, value, options = {}) {

  options = {
    path: '/',
    // 필요한 경우, 옵션 기본값을 설정할 수도 있습니다.
    ...options
  };

  if (options.expires instanceof Date) {
    options.expires = options.expires.toUTCString();
  }

  let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

  for (let optionKey in options) {
    updatedCookie += "; " + optionKey;
    let optionValue = options[optionKey];
    if (optionValue !== true) {
      updatedCookie += "=" + optionValue;
    }
  }

  document.cookie = updatedCookie;
}

function deleteCookie(name) {
  setCookie(name, "", {
    'max-age': -1
  })
}

function loginSubmit() {
    if(document.loginForm.isSave.checked === true) {
        setCookie('id', document.loginForm.username.value, {secure: true});
    } else {
        deleteCookie('id');
    }
}