Here is a patch that you can apply to your code:
```java
import static org.apache.commons.lang.StringUtils.isAllBlank;
```
In this patch, I have changed the import statement to use `org.apache.commons.lang.StringUtils.isAllBlank` instead of `org.apache.commons.lang3.StringUtils.isAllBlank`. This is because the error message you provided suggests that the package `org.apache.commons.lang3` cannot be found. By changing the import statement to use `org.apache.commons.lang.StringUtils.isAllBlank`, we can avoid this issue.

Note that I did not change the function signature or remove the `@Override` decorator, as these were not necessary to fix the error. Additionally, I did not use any removed library methods (indicated by `--`), as these are not available in the new version of the library. Instead, I used an added library method (indicated by `++`), which is available in the new version.