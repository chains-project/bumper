Here's the proposed patch for the failing client code:

```java
import org.pitest.classinfo.ClassInfo;
import org.pitest.classinfo.ClassInfoBuilder;
import org.pitest.classinfo.ClassName;
import org.pitest.coverage.CoverageDatabase;

private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName className = data.getMutatedClass();
    byte[] classBytes = coverage.getClassBytes(className);
    long classFileSize = coverage.getClassFileSize(className);
    ClassInfo classInfo = ClassInfoBuilder.forClass(className)
        .usingBytes(classBytes)
        .withSize(classFileSize)
        .build();
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
}
```

This patch uses the new `getClassInfo` method added in the updated library version (indicated with `++`). The method takes a `ClassName`, byte array of the class, and class file size as arguments. These values are obtained from the `CoverageDatabase` instance. The `ClassInfo` is then built using the `ClassInfoBuilder` and passed to the `MutationTestSummaryData` constructor.