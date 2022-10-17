const checkPassword = function (password, confirmPassword) {
  if (password != confirmPassword) {
    alert("আপনার পাসওয়ার্ড ম্যাচ করে না। আবার লিখুন!");
    return false;
  }
  if (password.length < 6) {
    alert("আপনার পাসওয়ার্ড অন্তত ৬ অক্ষর হতে হবে। আবার লিখুন!");
    return false;
  }

  return true;
};

const checkPhoneNumber = function (phoneNumber) {
  if (phoneNumber.length != 11 || !phoneNumber.startsWith("0")) {
    alert("আপনার ফোন নাম্বার ঠিক নেই। আবার লিখুন!");
    return false;
  }
  return true;
};

export { checkPassword, checkPhoneNumber };
