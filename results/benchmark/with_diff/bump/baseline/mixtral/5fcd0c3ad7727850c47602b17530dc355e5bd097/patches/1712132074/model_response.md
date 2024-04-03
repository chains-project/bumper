Based on the error message and the library changes, it seems that the `getClassInfo` method of `CoverageDatabase` is no longer available in the new library version. Instead, there is a new `getClassInfo` static method in `ClassInfoBuilder` that can be used. Here is a possible patch for the failing method:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    byte[] classBytes = coverage.getClassBytes(mutatedClass);
    long timestamp = coverage.getTimestamp(mutatedClass);
    ClassInfo classInfo = ClassInfoBuilder.getClassInfo(mutatedClass, classBytes, timestamp);
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

In this patch, we first retrieve the class bytes and timestamp from the `CoverageDatabase` using the existing methods. Then, we use the new `getClassInfo` method in `ClassInfoBuilder` to create a `ClassInfo` object from the class bytes and timestamp. Finally, we create a new `MutationTestSummaryData` object using the original method signature.

Note that this patch assumes that the `ClassMutationResults` class has a method `getMutatedClass()` that returns a `ClassName` object. If this is not the case, you may need to adjust the patch accordingly.