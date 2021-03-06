package apiutil

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
	"strings"

	"github.com/gocontrib/auth"
	"github.com/gocontrib/pubsub"
)

const (
	TypeJSON = "application/json"
)

// TODO later implement persistence of events for some period of time
func SendEvent(user auth.User, evt *pubsub.Event) {
	go func() {
		chans := []string{
			"global",
			fmt.Sprintf("%s/%s", evt.ResourceType, evt.ResourceID),
			fmt.Sprintf("user/%s", user.GetID()),
		}
		pubsub.Publish(chans, evt)
	}()
}

func SendJSON(w http.ResponseWriter, data interface{}, status ...int) error {
	w.Header().Set("Content-Type", TypeJSON)

	if len(status) > 0 {
		w.WriteHeader(status[0])
	}

	marshaller, ok := data.(json.Marshaler)
	if ok {
		b, err := marshaller.MarshalJSON()
		if err != nil {
			// TODO check whether it is possible to send error at this phase
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return err
		}
		w.Write(b)
		return nil
	}

	err := json.NewEncoder(w).Encode(data)
	if err != nil {
		// TODO check whether it is possible to send error at this phase
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return err
	}

	return nil
}

func SendError(w http.ResponseWriter, err error, status ...int) {
	if len(status) == 0 {
		errstr := err.Error()
		if strings.Contains(errstr, "not valid") || strings.Contains(errstr, "invalid") {
			status = []int{http.StatusBadRequest}
		} else if strings.Contains(errstr, "not found") {
			status = []int{http.StatusNotFound}
		} else {
			status = []int{http.StatusInternalServerError}
		}
	}

	data := &struct {
		Error string `json:"error"`
	}{
		Error: err.Error(),
	}
	SendJSON(w, data, status...)
}

type Pagination struct {
	Offset int
	Limit  int
}

func ParsePagination(r *http.Request) (result Pagination, err error) {
	offset, err := parseIntParam(r, "offset", 0, true, false)
	if err != nil {
		return result, err
	}

	limit, err := parseIntParam(r, "limit", 100, true, false)
	if err != nil {
		return result, err
	}

	result.Offset = int(offset)
	result.Limit = int(limit)

	return result, nil
}

func parseIntParam(r *http.Request, name string, defval int, nonNegative, positive bool) (int, error) {
	s := strings.TrimSpace(r.URL.Query().Get(name))
	if len(s) == 0 {
		return defval, nil
	}
	val, err := strconv.ParseInt(s, 10, 32)
	if err != nil {
		return 0, fmt.Errorf("%s param is not valid: expect integer number. %s", name, err)
	}
	if nonNegative && val < 0 {
		return 0, fmt.Errorf("%s param is not valid: expect non negative integer number", name)
	}
	if positive && val <= 0 {
		return 0, fmt.Errorf("%s param is not valid: expect positive integer number", name)
	}
	return int(val), nil
}
