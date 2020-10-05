// GET /17261/full/max/0/default.jpg. Requests an image with id 17261 with full region, max size, no rotation and default quality in jpg format.

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://munch.emuseum.com/apis/iiif/image/v2/17261/full/max/0/default.jpg"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


// GET /17261/90,0,350,220/max/0/default.jpg. Requests a reqion of an image with ID 17261 with max size, no rotation, default quality and jpg format.

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://munch.emuseum.com/apis/iiif/image/v2/17261/90,0,350,220/max/0/default.jpg"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


// GET /17261/90,0,350,220/max/90/default.jpg. Requests a region of an image with ID 17261 with max size, 90° rotation, default quality and jpg format.

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://munch.emuseum.com/apis/iiif/image/v2/17261/90,0,350,220/max/90/default.jpg"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


// GET /17261/info.json. Requests image information.

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://munch.emuseum.com/apis/iiif/image/v2/17261/info.json"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}
