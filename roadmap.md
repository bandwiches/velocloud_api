**Next Model: device_settings.py**

- Declare Optional vs Required attributes for models
- Determine what can be done with `enterprise_object_base`
  - Is this even used anywhere?  Can it be used anywhere?
- Figure out what's up with dictionary values in dataclasses
  - Create new objects for these specific things, use __repr__ to show as dict?
  - Just allow as dict() ?
- Find better naming structures for "custom classes" if it's decided to continue using them



Rules:
- If the model exists in the API, build it
- models can have `from_dict()` methods but they cannot directly call the API
  - Orchestrator will be used to call the API, build the model, and return the class filled object
  - `Session()` will be required to do any of this
    - Need to build a keepalive every 30 sec...output to stdout when it renews!
- If a model utilizes a k/v parameter that **IS NOT** a model, build it within that model
  - otherwise it's a real model so build it like a normal model
- If a model utilizes a blank `dict` parameter, just accept any `dict`
- I don't know wtf `< * > ` is, but it's annoying so i guess just accept a custom class with `data` as the sole attribute.