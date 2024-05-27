Here is the patched method:

```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return org.hamcrest.CoreMatchers.not(org.hamcrest.CoreMatchers.stringContains(String.format("%s: Pushed", this.image.layer())));
}
```

The changes I made are:

* Replace `new org.hamcrest.core.IsNot` with `org.hamcrest.CoreMatchers.not`
* Replace `new org.hamcrest.core.StringContains` with `org.hamcrest.CoreMatchers.stringContains`
* Replace `new org.hamcrest.core.IsNot(new org.hamcrest.core.StringContains(...))` with `org.hamcrest.CoreMatchers.not(org.hamcrest.CoreMatchers.stringContains(...))`

This should fix the error by using the added methods instead of the removed ones, and also simplifying the code.