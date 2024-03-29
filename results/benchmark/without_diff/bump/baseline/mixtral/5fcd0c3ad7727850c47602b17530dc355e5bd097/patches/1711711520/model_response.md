Sure, I understand the constraints. Here's a possible patch for the failing method:
```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(data.getMutatedClass());
    if (classInfo == null) {
        classInfo = new ClassInfoImpl(data.getMutatedClass(), Collections.emptyList());
    }
    return new MutationTestSummaryData(data.getFileName(),
            data.getMutations(), classInfo);
}
```
In this patch, we first get the `ClassInfo` object for the mutated class from the `CoverageDatabase`. If it's `null`, we create a new `ClassInfo` object with an empty list of methods. Then, we create a new `MutationTestSummaryData` object using the method parameters and the newly created or retrieved `ClassInfo` object.

Note that this patch assumes that the `ClassInfoImpl` class is a valid class that can be used as a replacement for `ClassInfo` if the original object is `null`. If this is not the case, you may need to adjust the patch accordingly.