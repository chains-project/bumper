Sure, here's the patched code:
```java
private static Matcher<String> imagePulled(String image) {
    String msg = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(msg);
}
```
I created a variable `msg` to make the code easier to read. I also removed the unnecessary `final` keyword from the `image` parameter.