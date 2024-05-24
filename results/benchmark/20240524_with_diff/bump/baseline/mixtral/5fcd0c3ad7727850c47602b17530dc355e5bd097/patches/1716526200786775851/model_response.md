Here's the proposed patch to fix the error:

```java
import org.pitest.classinfo.ClassInfo;
import org.pitest.classinfo.ClassInfoBuilder;
import org.pitest.classinfo.ClassName;
import org.pitest.coverage.CoverageDatabase;

private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName className = ClassName.classNamed(data.getMutatedClass());
    byte[] classBytes = coverage.getRawClassBytes(className);
    long timestamp = coverage.getTimestamp(className);
    ClassInfo classInfo = ClassInfoBuilder.buildFrom(className, classBytes, timestamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
}
```

In the patched code, we use the new `getClassInfo` method from the `ClassInfoVisitor` class to build the `ClassInfo` object directly from the raw class bytes and timestamp obtained from the `CoverageDatabase` object. This avoids the need to use the deprecated `getClassInfo` method from the `CoverageDatabase` class.