Here's a possible patch for the client code to fix the error caused by the removed `getClassInfo` method from `CoverageDatabase`:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder builder = org.pitest.classinfo.ClassInfo.builder(data.getMutatedClass());
    coverage.getRawCoverage(data.getMutatedClass()).ifPresent(rawCoverage -> {
        for (byte[] bytes : rawCoverage.getMethodData()) {
            builder.addMethod(org.pitest.classinfo.ClassInfo.fromBytecode(data.getMutatedClass(), bytes));
        }
    });
    org.pitest.classinfo.ClassInfo classInfo = builder.build();
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

This code creates a `ClassInfoBuilder` for the mutated class, then iterates over the raw coverage data to add method information to the builder. Finally, it builds the `ClassInfo` object and returns the `MutationTestSummaryData` object as before.

Note that this code assumes that the `getRawCoverage` method still exists in the `CoverageDatabase` class, and that it returns an `Optional` of `RawCoverage` for the given class name. If this assumption is incorrect, the code may need to be adjusted accordingly.